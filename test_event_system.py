from event_system import (
    book_ticket,
    can_book_ticket,
    cancel_event,
    can_check_in,
    can_enter_event,
    check_in,
    has_entry_pass,
    is_valid_age,
)


def make_event():
    return {
        "name": "Python Live",
        "is_event_open": True,
        "is_cancelled": False,
        "minimum_age": 18,
        "tickets_left": 5,
    }


def make_attendee():
    return {
        "name": "Alex",
        "age": 20,
        "has_ticket": False,
        "has_guest_pass": False,
        "has_valid_id": True,
        "is_checked_in": False,
    }


def test_is_valid_age_accepts_zero():
    assert is_valid_age(0) is True


def test_is_valid_age_rejects_negative_age():
    assert is_valid_age(-1) is False


def test_can_book_ticket_when_rules_are_met():
    event = make_event()
    attendee = make_attendee()

    assert can_book_ticket(event, attendee) is True


def test_cannot_book_when_no_tickets_are_left():
    event = make_event()
    attendee = make_attendee()
    event["tickets_left"] = 0

    assert can_book_ticket(event, attendee) is False


def test_book_ticket_changes_state_when_booking_succeeds():
    event = make_event()
    attendee = make_attendee()

    result = book_ticket(event, attendee)

    assert result is True
    assert event["tickets_left"] == 4
    assert attendee["has_ticket"] is True


def test_book_ticket_does_not_change_state_when_booking_is_rejected():
    event = make_event()
    attendee = make_attendee()
    event["tickets_left"] = 0

    result = book_ticket(event, attendee)

    assert result is False
    assert event["tickets_left"] == 0
    assert attendee["has_ticket"] is False


def test_check_in_changes_state_when_entry_is_allowed():
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True

    result = check_in(event, attendee)

    assert result is True
    assert attendee["is_checked_in"] is True


def test_check_in_does_not_change_state_without_entry_pass():
    event = make_event()
    attendee = make_attendee()

    result = check_in(event, attendee)

    assert result is False
    assert attendee["is_checked_in"] is False
    assert event["tickets_left"] == 5


# ============================================================
# YOUR TURN
# Add tests for the remaining functions:
# has_entry_pass()
# can_enter_event()
# can_check_in()
# cancel_event()
# ============================================================
