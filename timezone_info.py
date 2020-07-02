from datetime import datetime, timedelta
import pytz


def time_delta_seconds(str_time, fmt):
    user_date_time = datetime.strptime(str_time, fmt)
    user_time = timedelta(hours=user_date_time.hour, minutes=user_date_time.minute)

    now = datetime.utcnow()
    now_time = timedelta(hours=now.hour, minutes=now.minute)

    return (user_time - now_time).total_seconds()


def possible_timezones(tz_offset_seconds, common_only=True):
    # pick one of the timezone collections
    timezones = pytz.common_timezones if common_only else pytz.all_timezones

    # convert the float hours offset to a timedelta
    offset_days, offset_seconds = 0, tz_offset_seconds
    if offset_seconds < 0:
        offset_days = -1
        offset_seconds += 24 * 3600
    desired_delta = timedelta(offset_days, offset_seconds)

    # Loop through the timezones and find any with matching offsets
    null_delta = timedelta(0, 0)
    results = []
    for tz_name in timezones:
        tz = pytz.timezone(tz_name)
        non_dst_offset = getattr(tz, '_transition_info', [[null_delta]])[-1]
        diff = abs((desired_delta - non_dst_offset[0]).total_seconds())

        if diff <= 600: #5 minute
            results.append((tz_name,diff))

    return None if len(results)==0 else sorted(results, key=lambda t:t[1])[0][0]