from view.view import menuList, productList, productInput, productUpdate, productDelete
from controller.controller import ProductController

controller = ProductController()
controller.loadData()
while True:
    menu = menuList()
    if menu==0:
        controller.saveData()
        break
    elif menu==1:
        productList(controller.getAll())
    elif menu==2:
        controller.register(productInput())
    elif menu==3:
        (index, name, price) = productUpdate(controller.getAll())
        controller.update(index, name, price)
    elif menu==4:
        index = productDelete(controller.getAll())
        controller.delete(index)