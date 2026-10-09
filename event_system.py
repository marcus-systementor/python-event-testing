"""Validation and operations for a small concert event."""


def is_valid_age(age):
    return age >= 0


def has_entry_pass(attendee):
    return attendee["has_ticket"] or attendee["has_guest_pass"]


def can_book_ticket(event, attendee):
    is_open = event["is_event_open"]
    is_not_cancelled = not event["is_cancelled"]
    has_tickets_left = event["tickets_left"] > 0
    does_not_have_ticket = not attendee["has_ticket"]
    return is_open and is_not_cancelled and has_tickets_left and does_not_have_ticket


def book_ticket(event, attendee):
    if not can_book_ticket(event, attendee):
        return False

    event["tickets_left"] -= 1
    attendee["has_ticket"] = True
    return True


def can_enter_event(event, attendee):
    is_open = event["is_event_open"]
    is_not_cancelled = not event["is_cancelled"]
    has_pass = has_entry_pass(attendee)
    has_id = attendee["has_valid_id"]
    has_valid_age = is_valid_age(attendee["age"])
    is_old_enough = attendee["age"] >= event["minimum_age"]
    return is_open and is_not_cancelled and has_pass and has_id and has_valid_age and is_old_enough


def can_check_in(event, attendee):
    return can_enter_event(event, attendee) and not attendee["is_checked_in"]


def check_in(event, attendee):
    if not can_check_in(event, attendee):
        return False

    attendee["is_checked_in"] = True
    return True


def cancel_event(event):
    if event["is_cancelled"]:
        return False

    event["is_cancelled"] = True
    event["is_event_open"] = False
    return True
