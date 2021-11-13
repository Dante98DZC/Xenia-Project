from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from django.db.models import F

from core.express.models import Report, Departament


class ReportResource(resources.ModelResource):
    departament = Field(column_name=Departament._meta.verbose_name, attribute="departament")

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            att_name = field.attribute
            try:
                model_field = Report._meta.get_field(att_name)
                column_name = model_field.verbose_name
                field.column_name = column_name
            except:
                pass
        return fields

    def get_queryset(self):
        return super(ReportResource, self).get_queryset().annotate(**{"departament": F("attendant__dpt__name_dpt")})

    def dehydrate_executive(self, obj):
        return f"{obj.executive.first_name} {obj.executive.last_name}"

    def get_boolean_result(self, value):
        if value:
            return "Sí"
        return "No"

    def dehydrate_solved(self, obj):
        return self.get_boolean_result(obj.solved)

    def dehydrate_agree(self, obj):
        return self.get_boolean_result(obj.agree)

    def dehydrate_kind(self, obj):
        return str(obj.kind)

    def dehydrate_attendant(self, obj):
        return str(obj.attendant)

    class Meta:
        model = Report
        export_order = Report.get_fields_priority()
