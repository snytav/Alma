from xml.dom.minidom import parse
import numpy as np

def xread(filename):
    # parse an xml file by name
    mydoc = parse(filename)

    items = mydoc.getElementsByTagName('ImageData')

    # one specific item attribute
    print('Item #0 attribute:')
    print(items[0].attributes['Origin'].value)
    print(items[0].attributes['Spacing'].value)
    print(items[0].attributes['WholeExtent'].value)
    fields = mydoc.getElementsByTagName('DataArray')
    for fd in fields:
        name = fd.attributes['Name'].value
        child = fd.childNodes
        text = child[0].data
        nums_str = text.split(' ')
        for i in range(0,len(nums_str)):
            if nums_str[i] == '\n':
               nums_str.pop(i)
        nums = [float(i) for i  in nums_str]

        if name == 'NodeVol':
            total_len = len(nums)
            nx = int(pow(total_len,1.0/3.0))+1
            ny = nx
            nz = nx
            node_vol = np.asarray(nums)
            node_vol = node_vol.reshape(nx,ny,nz)

        if name == 'ef':
            ef = nums

        if name == 'phi':
            phi = nums

        if name == 'rho':
            rho = nums

        if name == 'nd.O+':
            ndp = nums

        if name == 'nd.e-':
            ndm = nums



        #l1 = ' '.join(t.nodeValue for t in name[0].childNodes if t.nodeType == t.TEXT_NODE)

    return

    # all item attributes
    print('\nAll attributes:')
    for elem in items:
        print(elem.attributes['name'].value)

    # one specific item's data
    print('\nItem #2 data:')
    print(items[1].firstChild.data)
    print(items[1].childNodes[0].data)

    # all items data
    print('\nAll item data:')
    for elem in items:
        print(elem.firstChild.data)


    return
    dom = parse(filename)
    name = dom.getElementsByTagName('DataArray')
    print( ' '.join(t.nodeValue for t in name[0].childNodes if t.nodeType == t.TEXT_NODE))
