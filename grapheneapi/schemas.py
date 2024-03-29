import graphene
from graphene_django import DjangoObjectType

from apps.accounts.models import Account, Address
from apps.markets.models import Market, Category, Product
from apps.support.models import ChatSupport, MarketSupport, NotificationSupport


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class MarketType(DjangoObjectType):
    class Meta:
        model = Market


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ChatSupportType(DjangoObjectType):
    class Meta:
        model = ChatSupport


class MarketSupportType(DjangoObjectType):
    class Meta:
        model = MarketSupport


class NotificationSupportType(DjangoObjectType):
    class Meta:
        model = NotificationSupport


class Query(graphene.ObjectType):
    account_model = graphene.List(AccountType)
    address_model = graphene.List(AddressType)
    market_model = graphene.List(MarketType)
    category_model = graphene.List(CategoryType)
    product_model = graphene.List(ProductType)
    chat_support_model = graphene.List(ChatSupportType)
    market_support_model = graphene.List(MarketSupportType)
    notification_support_model = graphene.List(NotificationSupportType)

    def resolve_account_model(self, info):
        return Account.objects.all()
    
    def resolve_address_model(self, info):
        return Address.objects.all()
    
    def resolve_market_model(self, info):
        return Market.objects.all()
    
    def resolve_category_model(self, info):
        return Category.objects.all()
    
    def resolve_product_model(self, info):
        return Product.objects.all()
     
    def resolve_chat_support_model(self, info):
        return ChatSupport.objects.all()
    
    def resolve_market_support_model(self, info):
        return MarketSupport.objects.all()
    
    def resolve_notification_support_model(self, info):
        return NotificationSupport.objects.all()
    

