from Event import Event


def test_a_listenner_is_notified_when_an_event_is_raised(mocker):
    listener = mocker.Mock()
    event = Event()
    event.connect(listener)
    event.fire()
    assert listener.called == True


def test_a_listener_is_passed_right_parameters(mocker):
    listener = mocker.Mock()
    event = Event()
    event.connect(listener)
    event.fire(5, shape="square")
    listener.assert_called_with(5, shape="square")
