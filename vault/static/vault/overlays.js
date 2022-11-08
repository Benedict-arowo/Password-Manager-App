const addFolder = document.getElementById('addFolder');
const overlays = document.getElementById('overlays');

const ItemForm = document.getElementById('ItemForm');
const FolderForm = document.getElementById('FolderForm');
const DeleteForm = document.getElementById('DeleteForm');

const cancelBtns = document.querySelectorAll('.cancelForm');
const deleteBtns = document.querySelectorAll('.deleteBtn')
const editBtns = document.querySelectorAll('.editBtn')
const cancelBtn = document.getElementById('cancelBtn');

const addItem = document.getElementById('addItem');
const itemType = document.getElementById('itemtype')
const deleteLink = document.getElementById('deleteLink')

overlays.addEventListener('click', e => {
    // Hides the overlay element whenever it's clciked, with a fade out effect.
    if (e.target.id == 'overlays') {
        overlays.style.opacity = '0'
        setTimeout(() => {
            overlays.style.display = ''
        }, 100)
    }
})

const updateDisplay = (element) => {
    overlays.style.opacity = '1'
    ItemForm.style.display = element == 'item' ? 'flex' : ''
    FolderForm.style.display = element == 'folder' ? 'grid' : ''
    DeleteForm.style.display = element == 'delete' ? 'grid' : ''
}

addItem.addEventListener('click', e => {
    overlays.style.display = 'grid'
    overlays.style.opacity = '0'

    // Fade in effect, and showing the overlay element
    setTimeout(updateDisplay('item'), 100)
})

cancelBtns.forEach(btn => {
    btn.addEventListener('click', e => {
        e.preventDefault()
        // Fade in effect, and hiding the overlay element
        overlays.style.opacity = '0'
        setTimeout(() => {
            overlays.style.display = ''
        }, 100)
    })
})

addFolder.addEventListener('click', e => {
    overlays.style.display = 'grid'
    overlays.style.opacity = '0'

    // Fade in effect, and showing the overlay element
    setTimeout(updateDisplay('folder'), 100)
})

DeleteForm.addEventListener('click', e => {
    overlays.style.display = 'grid'
    overlays.style.opacity = '0'

    // Fade in effect, and showing the overlay element
    setTimeout(updateDisplay('delete'), 100)
})

deleteBtns.forEach(btn => {
    btn.addEventListener('click', async e => {
        // For fade in effect 
        overlays.style.cssText = 'display: grid; opacity: 0;'
        id = e.target.dataset.id

        // Checks if the user is deleting an item or a folder, and updates the delete href link accordingly 
        if (e.target.dataset.type == 'item') {
            itemType.textContent = 'item'
            deleteLink.setAttribute('href', `deleteItem?id=${id}`)
        }
        else {
            itemType.textContent = 'folder'
            deleteLink.setAttribute('href', `deleteFolder?id=${id}`)
        }

        // Fade in effect, and showing the overlay element
        setTimeout(updateDisplay('delete'), 100)
    })
})


