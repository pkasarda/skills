def export(source,destination,settings):
    image=decode(source)
    result=resize(image,settings)
    write_image(destination,result)

