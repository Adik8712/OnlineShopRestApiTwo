import graphene
from graphene_django import DjangoObjectType

from apps.accounts.models import Account, Address
from apps.markets.models import Market, Category, Product
from apps.support.models import ChatSupport, MarketSupport

from grapheneapi.schemas import (
    AccountType,
    AddressType,
    
    MarketType,
    CategoryType,
    ProductType,
    
    ChatSupportType,
    MarketSupportType,
    # NotificationSupportType,
)

# POST for ChatSupport
class CreateChatSupport(graphene.Mutation):
    class Arguments:
        account_id = graphene.ID(required=True)
        message = graphene.String(required=True)
    
    chat_support = graphene.Field(ChatSupportType)

    def mutate(self, info, account_id, message):
        account = Account.objects.get(id=account_id)
        chat_support = ChatSupport.objects.create(account=account, message=message)
        
        return CreateChatSupport(chat_support=chat_support)


# PUT for ChatSupport
class UpdateChatSupport(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        message = graphene.String()

    chat_support = graphene.Field(ChatSupportType)

    def mutate(self, info, id, message=None):
        chat_support = ChatSupport.objects.get(id=id)

        if message:
            chat_support.message = message

        chat_support.save()
        return UpdateChatSupport(chat_support=chat_support)


# DELETE for ChatSupport
class DeleteChatSupport(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    chat_support = graphene.Field(ChatSupportType)

    def mutate(self, info, id):
        chat_support = ChatSupport.objects.get(id=id)
        chat_support.delete()

        return DeleteChatSupport(chat_support=None)


# POST for MarketSupport
class CreateMarketSupport(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        open_time = graphene.Time(required=True)
        close_time = graphene.Time(required=True)
        the_cost_of_delivery = graphene.Decimal(required=True)
        minimum_order = graphene.Decimal(required=True)
        maximum_distance_without_extra_charge = graphene.Decimal(required=True)
        address = graphene.String(required=True)
        phone_number = graphene.String(required=True)

    market_support = graphene.Field(MarketSupportType)

    def mutate(
            self, info, name, description, open_time, close_time, the_cost_of_delivery, 
            minimum_order, maximum_distance_without_extra_charge, address, phone_number
        ):
        market_support = MarketSupport.objects.create(
            name=name,
            description=description,
            open_time=open_time,
            close_time=close_time,
            the_cost_of_delivery=the_cost_of_delivery,
            minimum_order=minimum_order,
            maximum_distance_without_extra_charge=maximum_distance_without_extra_charge,
            address=address,
            phone_number=phone_number
        )

        return CreateMarketSupport(market_support=market_support)
    

# PUT for MarketSupport
class UpdateMarketSupport(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()
        open_time = graphene.Time()
        close_time = graphene.Time()
        the_cost_of_delivery = graphene.Decimal()
        minimum_order = graphene.Decimal()
        maximum_distance_without_extra_charge = graphene.Decimal()
        address = graphene.String()
        phone_number = graphene.String()
    
    market_support = graphene.Field(MarketSupportType)

    def mutate(
            self, info, id, 
            name=None, description=None, open_time=None, close_time=None, the_cost_of_delivery=None, 
            minimum_order=None, maximum_distance_without_extra_charge=None, 
            address=None, phone_number=None):
        
        market_support = MarketSupport.objects.get(id=id)

        if name:
            market_support.name = name
        
        if description:
            market_support.description = description
        
        if open_time:
            market_support.open_time = open_time
        
        if close_time:
            market_support.close_time = close_time
        
        if the_cost_of_delivery:
            market_support.the_cost_of_delivery = the_cost_of_delivery
        
        if minimum_order:
            market_support.minimum_order = minimum_order
        
        if maximum_distance_without_extra_charge:
            market_support.maximum_distance_without_extra_charge =maximum_distance_without_extra_charge
        
        if address:
            market_support.address = address
        
        if phone_number:
            market_support.phone_number = phone_number
        
        market_support.save()
        return UpdateMarketSupport(market_support=market_support)


# DALETE for MarketSupport
class DeleteMarketSupport(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    market_support = graphene.Field(MarketSupportType)

    def mutate(self, info, id):
        market_support = MarketSupport.objects.get(id=id)
        market_support.delete()
    
        return DeleteMarketSupport(market_support=None)


# POST for Market
class CreateMarket(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        open_time = graphene.Time(required=True)
        close_time = graphene.Time(required=True)
        the_cost_of_delivery = graphene.Decimal(required=True)
        minimum_order = graphene.Decimal(required=True)
        maximum_distance_without_extra_charge = graphene.Decimal(required=True)
        address = graphene.String(required=True)
        phone_number = graphene.String(required=True)

    market = graphene.Field(MarketType)

    def mutate(
            self, info, name, description, open_time, close_time, the_cost_of_delivery, 
            minimum_order, maximum_distance_without_extra_charge, address, phone_number
        ):
        market = Market.objects.create(
            name=name,
            description=description,
            open_time=open_time,
            close_time=close_time,
            the_cost_of_delivery=the_cost_of_delivery,
            minimum_order=minimum_order,
            maximum_distance_without_extra_charge=maximum_distance_without_extra_charge,
            address=address,
            phone_number=phone_number
        )

        return CreateMarket(market=market)


# PUT for Market
class UpdateMarket(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()
        open_time = graphene.Time()
        close_time = graphene.Time()
        the_cost_of_delivery = graphene.Decimal()
        minimum_order = graphene.Decimal()
        maximum_distance_without_extra_charge = graphene.Decimal()
        address = graphene.String()
        phone_number = graphene.String()
    
    market = graphene.Field(MarketType)

    def mutate(
            self, info, id, 
            name=None, description=None, open_time=None, close_time=None, the_cost_of_delivery=None, 
            minimum_order=None, maximum_distance_without_extra_charge=None, 
            address=None, phone_number=None):
        
        market = Market.objects.get(id=id)

        if name:
            market.name = name
        
        if description:
            market.description = description
        
        if open_time:
            market.open_time = open_time
        
        if close_time:
            market.close_time = close_time
        
        if the_cost_of_delivery:
            market.the_cost_of_delivery = the_cost_of_delivery
        
        if minimum_order:
            market.minimum_order = minimum_order
        
        if maximum_distance_without_extra_charge:
            market.maximum_distance_without_extra_charge =maximum_distance_without_extra_charge
        
        if address:
            market.address = address
        
        if phone_number:
            market.phone_number = phone_number
        
        market.save()
        return UpdateMarket(market=market)
    

# DELETE for Market
class DeleteMarket(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    market = graphene.Field(MarketType)

    def mutate(self, info, id):
        market = Market.objects.get(id=id)
        market.delete()
    
        return DeleteMarket(market=None)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, description):
        category = Category.objects.create(name=name, description=description)

        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()
    
    category = graphene.Field(CategoryType)

    def mutate(self, info, id, name=None, description=None):
        category = Category.objects.get(id=id)

        if name:
            category.name = name

        if description:
            category.description = description

        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, id):
        category = Category.objects.get(id=id)
        category.delete()

        return DeleteCategory(category=None)


class CreateProduct(graphene.Mutation):
    class Arguments:
        market = graphene.ID(required=True)
        image = graphene.String(required=True)
        code = graphene.String(required=True)
        name = graphene.String(required=True)
        brand = graphene.String()
        category = graphene.ID(required=True)
        price = graphene.Decimal(required=True)
        stock = graphene.Int()
        description = graphene.String()
        calories = graphene.Float()
        fat = graphene.Float()
        carbohydrates = graphene.Float()
        protein = graphene.Float()
        fiber = graphene.Float()
    
    product = graphene.Field(ProductType)

    def mutate(
            self, info, market, image, code, name, brand, category, price, stock, description,
            calories, fat, carbohydrates, protein, fiber
        ):
        product = Product.objects.create(
            market=market,
            image=image,
            code=code,
            name=name,
            brand=brand,
            category=category,
            price=price,
            stock=stock,
            description=description,
            calories=calories,
            fat=fat,
            carbohydrates=carbohydrates,
            protein=protein,
            fiber=fiber
        )

        return CreateProduct(product=product)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        image = graphene.String()
        code = graphene.String()
        name = graphene.String()
        brand = graphene.String()
        category = graphene.ID()
        price = graphene.Decimal()
        stock = graphene.Int()
        description = graphene.String()
        calories = graphene.Float()
        fat = graphene.Float()
        carbohydrates = graphene.Float()
        protein = graphene.Float()
        fiber = graphene.Float()
    
    product = graphene.Field(ProductType)

    def mutate(
            self, info, id, image=None, code=None, name=None, brand=None, category=None, price=None, stock=None,
            description=None, calories=None, fat=None, carbohydrates=None, protein=None, fiber=None
        ):
        product = Product.objects.get(id=id)

        if image:
            product.image = image

        if code:
            product.code = code
        
        if name:
            product.name = name
        
        if brand:
            product.brand = brand
        
        if category:
            category = Category.objects.get(id=category)
            product.category = category
        
        if price:
            product.price = price
        
        if stock:
            product.stock = stock
        
        if description:
            product.description = description
        
        if calories:
            product.calories = calories
        
        if fat:
            product.fat = fat
        
        if carbohydrates:
            product.carbohydrates = carbohydrates
        
        if protein:
            product.protein = protein
        
        if fiber:
            product.fiber = fiber
        
        product.save()
        return UpdateProduct(product=product)


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    product = graphene.Field(ProductType)

    def mutate(self, info, id):
        product = Product.objects.get(id=id)
        product.delete()

        return DeleteProduct(product=None)


class CreateAddress(graphene.Mutation):
    class Arguments:
        city = graphene.String(required=True)
        street = graphene.String(required=True)
        house = graphene.String(required=True)
        flat = graphene.String(required=True)
        other = graphene.String()
    
    address = graphene.Field(AddressType)

    def mutate(self, info, city, street, house, flat, other):
        address = Address.objects.create(
            city=city,
            street=street,
            house=house,
            flat=flat,
            other=other
        )

        return CreateAddress(address=address)


class UpdateAddress(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        city = graphene.String()
        street = graphene.String()
        house = graphene.String()
        flat = graphene.String()
        other = graphene.String()
    
    address = graphene.Field(AddressType)

    def mutate(self, info, id, city=None, street=None, house=None, flat=None, other=None):
        address = Address.objects.get(id=id)

        if city:
            address.city = city

        if street:
            address.street = street

        if house:
            address.house = house

        if flat:
            address.flat = flat

        if other:
            address.other = other

        address.save()
        return UpdateAddress(address=address)


class DeleteAddress(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    address = graphene.Field(AddressType)

    def mutate(self, info, id):
        address = Address.objects.get(id=id)
        address.delete()

        return DeleteAddress(address=None)


class CreateAccount(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        username = graphene.String(required=True)

    account = graphene.Field(AccountType)

    def mutate(self, info, email, password, username):
        account = Account.objects.create_user(
            email=email,
            password=password,
            username=username
        )

        return CreateAccount(account=account)


class UpdateAccount(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        email = graphene.String()
        password = graphene.String()
        username = graphene.String()

    account = graphene.Field(AccountType)

    def mutate(self, info, id, email=None, password=None, username=None):
        account = Account.objects.get(id=id)

        if email:
            account.email = email

        if password:
            account.password = password

        if username:
            account.username = username

        account.save()
        return UpdateAccount(account=account)
    

class DeleteAccount(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    account = graphene.Field(AccountType)

    def mutate(self, info, id):
        account = Account.objects.get(id=id)
        account.delete()

        return DeleteAccount(account=None)


class Mutation(graphene.ObjectType):
    create_chat_support = CreateChatSupport.Field()
    update_chat_support = UpdateChatSupport.Field()
    delete_chat_support = DeleteChatSupport.Field()

    create_market_support = CreateMarketSupport.Field()
    update_market_support = UpdateMarketSupport.Field()
    delete_market_support = DeleteMarketSupport.Field()

    create_market = CreateMarket.Field()
    update_merket = UpdateMarket.Field()
    delete_market = DeleteMarket.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

    create_address = CreateAddress.Field()
    update_address = UpdateAddress.Field()
    delete_address = DeleteAddress.Field()

    create_account = CreateAccount.Field()
    update_account = UpdateAccount.Field()
    delete_account = DeleteAccount.Field()