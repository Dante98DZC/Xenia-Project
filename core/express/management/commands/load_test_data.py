import random
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from core.express.models import (Attendant, Client, ClientOb, ClientRoom,
                                 Departament, Executive, KindRep, Observ,
                                 Report, Responce, Room, RoomState)


class Command(BaseCommand):
    help = "Create test data"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Creating data"))
        self.stdout.write(self.style.SUCCESS("Creating RoomState"))
        ready_state = RoomState.objects.create(room_state="Listo")
        ocu_state = RoomState.objects.create(room_state="Ocupado")
        out_state = RoomState.objects.create(room_state="Fuera de servicio")
        self.stdout.write(self.style.SUCCESS("Creating Room"))
        r1 = Room.objects.create(state=ready_state)
        r2 = Room.objects.create(state=ready_state)
        r3 = Room.objects.create(state=ready_state)
        r4 = Room.objects.create(state=ocu_state)
        r5 = Room.objects.create(state=ocu_state)
        r6 = Room.objects.create(state=ocu_state)
        r7 = Room.objects.create(state=out_state)
        r8 = Room.objects.create(state=out_state)
        r9 = Room.objects.create(state=out_state)
        self.stdout.write(self.style.SUCCESS("Creating Observ"))
        o1 = Observ.objects.create(observ_name="Buena")
        o2 = Observ.objects.create(observ_name="Mala")
        o3 = Observ.objects.create(observ_name="Aceptable")
        self.stdout.write(self.style.SUCCESS("Creating Client"))
        c1 = Client.objects.create(
            id=str(int(random.random() * 99999999999)),
            first_name="Jhon",
            last_name="Doe",
            fly="123-Airline",
            agency="InterSpace",
            arrive_date=datetime.now(),
            leave_date=datetime.now(),
        )
        c1.rooms.add(r1)
        c1.rooms.add(r4)
        c1.observations.add(o1)
        c1.observations.add(o2)
        c1.save()
        c2 = Client.objects.create(
            id=str(int(random.random() * 99999999999)),
            first_name="Jane",
            last_name="Doe",
            fly="124-Airline",
            agency="InterSpace",
            arrive_date=datetime.now(),
            leave_date=datetime.now(),
        )
        c2.rooms.add(r2)
        c2.rooms.add(r5)
        c2.observations.add(o2)
        c2.observations.add(o3)
        c2.save()
        self.stdout.write(self.style.SUCCESS("Creating Departament"))
        d1 = Departament.objects.create(
            name_dpt="Departament of Mail", phone_number="555-12-555"
        )
        d2 = Departament.objects.create(
            name_dpt="Departament of Service", phone_number="515-12-515"
        )
        self.stdout.write(self.style.SUCCESS("Creating Attendant"))
        at1 = Attendant.objects.create(
            ci_attendant=str(int(random.random() * 99999999999)),
            first_name="Mark",
            last_name="Doe",
            dpt=d1,
        )
        at2 = Attendant.objects.create(
            ci_attendant=str(int(random.random() * 99999999999)),
            first_name="Shade",
            last_name="Doe",
            dpt=d2,
        )
        self.stdout.write(self.style.SUCCESS("Creating KindRep"))
        k1 = KindRep.objects.create(name_kind="Urgente")
        k2 = KindRep.objects.create(name_kind="Semanal")
        self.stdout.write(self.style.SUCCESS("Creating Executive"))
        e1 = Executive.objects.create(
            user_name="jd",
            ci_executive=str(int(random.random() * 99999999999)),
            first_name="Otto",
            last_name="Doe",
        )
        e2 = Executive.objects.create(
            user_name="jz",
            ci_executive=str(int(random.random() * 99999999999)),
            first_name="Liz",
            last_name="Doe",
        )
        self.stdout.write(self.style.SUCCESS("Creating Responce"))
        re1 = Responce.objects.create(description="Problema resuelto")
        re2 = Responce.objects.create(description="Problema descartado")
        self.stdout.write(self.style.SUCCESS("Creating Report"))
        Report.objects.create(
            client_room=ClientRoom.objects.first(),
            executive=e1,
            attendant=at1,
            kind=k1,
            description="Iluminacion defectuosa",
            response_date_time=datetime.now(),
            responsed=True,
            responce=re1,
        )
        Report.objects.create(
            client_room=ClientRoom.objects.last(),
            executive=e2,
            attendant=at2,
            kind=k2,
            description="Baño defectuoso",
            response_date_time=datetime.now(),
            responsed=True,
            responce=re2,
        )
        self.stdout.write(self.style.SUCCESS("DONE!"))
        self.stdout.write(self.style.SUCCESS("DONE!"))
