document.addEventListener('DOMContentLoaded', function(){
    if (loggedIn){
        const login = document.getElementById('login_button');
        const logout = document.createElement('a');
        logout.href = '/logout';
        logout.id='logout_button';
        logout.textContent = "Sign Out";

        login.replaceWith(logout);
    }
    else{
        const profile = document.getElementById('pbutton');
        const login = document.createElement('a');
        login.href = '/signin';
        login.id = 'pbutton';
        login.textContent = "Profile";  

        profile.replaceWith(login)  
    }

    page = document.title;
    
    if(page == "Filter"){
        const filter = document.getElementById('filters')
        var cselect = false;
        var sbutton = false;
        document.getElementById('category').addEventListener('change', function() {
            var category = document.getElementById('category').value;
            if (category != ''){
                if (!cselect){
                    cselect = true;
                    // Displaying additional filters
                    const newFilter = document.createElement('div');
                    newFilter.classList.add('relative', 'inline-block', 'w-1/2', 'my-7', 'border', 'border-purple-800', 'rounded-md', 'p-10', 'border-solid');
                    const label = document.createElement('label');
                    label.setAttribute('for', 'values');
                    label.classList.add('block', 'text-lg', 'font-medium', 'text-gray-700');
                    label.textContent = 'Choose value range';
                    newFilter.appendChild(label);
                    const options = document.createElement('select');
                    options.setAttribute('id', 'values');
                    options.setAttribute('name', 'values')
                    options.setAttribute('required', '')
                    options.classList.add('mt-1', 'block', 'w-full', 'rounded-md', 'border-gray-300', 'shadow-sm', 'focus:ring-indigo-500', 'focus:border-indigo-500', 'text-gray-700');

                    //default option
                    const o0 = document.createElement('option');
                    o0.setAttribute('disabled', '');
                    o0.setAttribute('selected', '');
                    o0.setAttribute('value', '');
                    o0.textContent = 'Select a Value Range';
                    options.appendChild(o0);

                    const o1 = document.createElement('option');
                    o1.setAttribute('value', '1');
                    o1.textContent = '1';
                    options.appendChild(o1);

                    newFilter.appendChild(options);
                    filter.appendChild(newFilter);
                }
                if (!sbutton){
                    sbutton = true;
                    //Display submit button
                    document.getElementById('values').addEventListener('change', function() {
                        var fdone = document.getElementById('values').value;
                        if(category !=''){
                            const submit = document.createElement('button');
                            submit.setAttribute('type', 'submit');
                            submit.classList.add('mt-3', 'w-1/2', 'px-4', 'py-2', 'bg-purple-800', 'text-white', 'rounded-md', 'hover:bg-purple-700', 'focus:outline-none', 'focus:ring-2', 'focus:ring-purple-500', 'focus:ring-offset-2');
                            submit.textContent='Submit';
                            filter.appendChild(submit);
                        }
                    });
                }
            }
        });
    }
});
