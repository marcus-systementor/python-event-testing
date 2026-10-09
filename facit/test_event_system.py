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


# ------------------------------------------------------------
# has_entry_pass()
# ------------------------------------------------------------


def test_has_entry_pass_is_true_with_ticket():
    attendee = make_attendee()
    attendee["has_ticket"] = True

    assert has_entry_pass(attendee) is True


def test_has_entry_pass_is_true_with_guest_pass():
    attendee = make_attendee()
    attendee["has_guest_pass"] = True

    assert has_entry_pass(attendee) is True


def test_has_entry_pass_is_false_without_ticket_and_guest_pass():
    attendee = make_attendee()

    assert has_entry_pass(attendee) is False


# ------------------------------------------------------------
# can_enter_event()
# ------------------------------------------------------------


def test_can_enter_event_when_rules_are_met():
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True

    assert can_enter_event(event, attendee) is True


def test_cannot_enter_event_when_under_minimum_age():
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    attendee["age"] = 17

    assert can_enter_event(event, attendee) is False


def test_cannot_enter_event_without_valid_id():
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    attendee["has_valid_id"] = False

    assert can_enter_event(event, attendee) is False


def test_can_enter_event_when_age_equals_minimum_age():
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    attendee["age"] = event["minimum_age"]

    assert can_enter_event(event, attendee) is True


def test_cannot_enter_event_without_entry_pass():
    event = make_event()
    attendee = make_attendee()

    assert can_enter_event(event, attendee) is False


def test_cannot_enter_cancelled_event():
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    event["is_cancelled"] = True

    assert can_enter_event(event, attendee) is False


# ------------------------------------------------------------
# can_check_in()
# ------------------------------------------------------------


def test_can_check_in_when_valid_and_not_checked_in():
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True

    result = can_check_in(event, attendee)

    assert result is True
    assert attendee["is_checked_in"] is False


def test_cannot_check_in_when_already_checked_in():
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    attendee["is_checked_in"] = True

    result = can_check_in(event, attendee)

    assert result is False
    assert attendee["is_checked_in"] is True


def test_cannot_check_in_when_not_allowed_to_enter():
    event = make_event()
    attendee = make_attendee()

    result = can_check_in(event, attendee)

    assert result is False
    assert attendee["is_checked_in"] is False


# ------------------------------------------------------------
# cancel_event()
# ------------------------------------------------------------


def test_cancel_event_closes_event():
    event = make_event()

    result = cancel_event(event)

    assert result is True
    assert event["is_cancelled"] is True
    assert event["is_event_open"] is False


def test_cancel_event_when_already_cancelled_changes_nothing():
    event = make_event()
    cancel_event(event)

    result = cancel_event(event)

    assert result is False
    assert event["is_cancelled"] is True
    assert event["is_event_open"] is False
