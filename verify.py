import os

def organization(path, typeOrg):
    """
    Parameters
    ----------
    path : string 
        it must be a string with the format r'...'

    Returns
    -------
    organization : list
        List of tuples with the folders and files within it.
    """
    
    organization = []
    if typeOrg == 0: 
        for root, folder, file in os.walk(path, topdown=True):
            tupla = folder, file
            organization.append(tupla)
            return organization
        #return organization
    
    if typeOrg == 1:
        for root, folder, file in os.walk(path, topdown=True):
            tupla = root, folder, file
            organization.append(tupla)
            return organization
        #return organization

def isEquals (old, new, core):
    """
    Parameters
    ----------
    old : list
        tuplas that contains the folders and files.
    new : list
        tuplas that contains the folders and files.
    core : list
        tuplas that contains the root, folders and files.

    Returns
    -------
    str
    """
    count = 0       
    while count <= len(old):
        if old[count] != new[count]:
            print('\nComo está o original:')
            print(f'Caminho onde está aparecendo dif.: {core[count][0]}')
            print(f'Pastas contidas nesse mesmo caminho: {core[count][1]}')
            print(f'Arquivos contidos nesse mesmo caminho: {core[count][2]}')
            
            print('\n')
            print('Como está o novo: ')
            print(f'Pastas contidas no novo: {new[count][0]}')
            print(f'Arquivos contidos no novo: {new[count][1]}')
            
            return '\n\n\nCorrija e rode novamente!!'
        count += 1
    return 'LISTO!!!!'
    
def main():
    #OBS.: o r em r'...' é para raw: ele desconcidera o \ que normanente é usado em comomandos como \n
    #sem o r teria que ser \\ para o \ ser conciderado como uma barra invertida
    oldPath = r'Z:\Shared Documents'
    newPath = r'C:\Users\PZSB7M\General Motors\GMSA Sales Intelligence Historical Data - Documents\Brazil\Sales Planning Statistics'
    
    organizeNew = organization(newPath, 0)
    organizeOld = organization(oldPath, 0)
    
    core = organization(oldPath, 1)
    
    print(isEquals(organizeOld, organizeNew, core))

main()       
        
