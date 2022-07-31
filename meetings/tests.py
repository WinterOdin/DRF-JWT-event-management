from .models import ConferenceLocation, Event
from auth_app.models import CustomUser
from django.test import TestCase
# Create your tests here.


class Test_Create_Event(TestCase):
    """
    I've created one test each because
        'We would like to see a unit test being showcased, but by any
        means please do not try ensuring 100% coverage.'

    """

    @classmethod
    def setUpTestData(cls) -> None:

        test_user = CustomUser.objects.create(
            email="test@tango.com", user_name="tango_test", password="T@ng0123$"
        )
        test_user.save()

        test_location = ConferenceLocation.objects.create(
            manager=test_user,
            name="tango_barista_course",
            location="tango_caffe",
            date_created="2022-07-30T23:02",
        )
        test_location.save()

        test_event = Event.objects.create(
            owner=test_user,
            place=test_location,
            name="test_name_event",
            agenda="test_agenda",
            start_date="2022-07-30 22:06",
            end_date="2022-07-30 23:46",
        )
        test_event.save()

    def test_event_content(self):
        event = Event.objects.get(id=1)
        user = CustomUser.objects.get(id=1)
        location = ConferenceLocation.objects.get(id=1)
        owner = f"{event.owner}"
        place = f"{event.place}"
        name = f"{event.name}"
        agenda = f"{event.agenda}"
        start_date = f"{event.start_date}"
        end_date = f"{event.end_date}"
        # testing some dunders
        self.assertEqual(
            str(location), "Conference room: tango_barista_course managed tango_test"
        )
        self.assertEqual(str(event), f"Event owner: {owner}")
        self.assertEqual(str(user), "tango_test")
        # testing event content
        self.assertEqual(owner, "tango_test")
        self.assertEqual(
            place, "Conference room: tango_barista_course managed tango_test"
        )
        self.assertEqual(name, "test_name_event")
        self.assertEqual(agenda, "test_agenda")
        self.assertEqual(start_date, "2022-07-30 22:06:00")
        self.assertEqual(end_date, "2022-07-30 23:46:00")
