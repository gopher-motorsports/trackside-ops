function clicked(event)
{
    if(!confirm('This will update the entry. Are you sure you want to continue?')){
        event.preventDefault()
    }
}