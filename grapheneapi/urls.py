import graphene

from django.contrib.auth.decorators import login_required
from django.urls import path

from graphene_django.views import GraphQLView

from grapheneapi.schemas import Query
from grapheneapi.mutation import Mutation


class CustomGraphQLView(GraphQLView):
    # def get_context(self, request):
    #     context = super().get_context(request)
    #     context["user"] = request.user
    #     return context

    def execute_graphql_request(
            self, request, data, query, variables, operation_name, show_graphiql=False
        ):
        return super().execute_graphql_request(
            request, data, query, variables, operation_name, show_graphiql
        )


@login_required(login_url='/admin')
def graphql_view(request):
    schema = graphene.Schema(query=Query, mutation=Mutation, auto_camelcase=True)
    view = CustomGraphQLView.as_view(graphiql=True, schema=schema)
    return view(request)


urlpatterns = [
    path('', graphql_view),
]