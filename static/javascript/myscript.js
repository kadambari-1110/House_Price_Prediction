function validation()
{
    bedroom = document.getElementsByName("bedroom")[0].value;
    bathroom = document.getElementsByName("bathroom")[0].value;
    balconies = document.getElementsByName("balcony")[0].value;
    parkings = document.getElementsByName("parking")[0].value;
    area = document.getElementsByName("area")[0].value;
    location = document.getElementsByName("location")[0].value;

    if (!bedroom )
    {
        window.alert("Enter the no of bedroom");
        window.location.href=window.location.href;
        return false;
    }
    
    if (!bathroom)
    {
        window.alert("Enter the no of bathrooms");
        window.location.href=window.location.href;
        return false;
    }
    
    if (!balconies)
    {
        window.alert("Enter the no of balconies");
        window.location.href=window.location.href;
        return false;
    }
    
    if (!parkings)
    {
        window.alert("Enter the no of parkings");
        window.location.href=window.location.href;
        return false;
    }
    
    if (!area)
    {
        window.alert("Enter the area");
        window.location.href=window.location.href;
        return false;
    }
    
    if (location==="")
    {
        window.alert("Enter the no of location");
        window.location.href=window.location.href;
        return false;
    }

    return true;
    
}
