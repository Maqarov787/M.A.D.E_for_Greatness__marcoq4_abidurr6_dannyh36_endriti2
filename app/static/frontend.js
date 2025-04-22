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
        var sbutton = false;
        var checked = false;
        document.getElementById('category').addEventListener('change', function() {
            var category = this.value;
            // Displaying additional filters
            const newFilter = document.createElement('div');
            newFilter.classList.add('relative', 'inline-block', 'w-1/2', 'my-7', 'border', 'border-purple-800', 'rounded-md', 'p-10', 'border-solid');
            newFilter.setAttribute('id', 'valuesF');
            const label = document.createElement('label');
            label.setAttribute('for', 'values');
            label.classList.add('block', 'text-lg', 'font-medium', 'text-gray-700', 'space-x-2');

            if (category == 'broadcast_day_of_the_week' || category == 'genres' || category == 'studios'){
                const ltext = document.createElement('p');
                ltext.textContent = 'Select Desired';
                label.appendChild(ltext);

                const em = document.createElement('p');
                em.setAttribute('id', 'em')
                em.classList.add('text-red-500', 'hidden')
                em.textContent = 'Please select at least one option!';

                label.appendChild(em);

                newFilter.appendChild(label);

                //each checkbox
                if (category == 'broadcast_day_of_the_week'){
                    const options = bdfw;
                }
                else if (category == 'genres'){
                    const options = genres;
                }
                else{
                    const options = studios;
                }

                for (const option of options){
                    const ol = document.createElement('label');
                    ol.classList.add('flex', 'items-center', 'space-x-2');

                    const o = document.createElement('input');
                    o.value =option;
                    o.setAttribute('name', 'values');
                    o.setAttribute('type', 'checkbox');
                    o.addEventListener('change', function() {
                        checked = true;
                    });

                    const ov = document.createElement('span');
                    ov.textContent = option;

                    ol.appendChild(o);
                    ol.appendChild(ov);
            
                    newFilter.appendChild(ol);
                }

            }
            else{
                label.textContent = 'Please select a minimum and maximum';
                newFilter.appendChild(label);
                newFilter.classList.add('space-y-2')

                const minl = document.createElement('label');
                minl.classList.add('flex', 'items-center', 'space-x-2', 'block', 'text-md', 'text-gray-700',);

                const min = document.createElement('input');
                min.setAttribute('name', 'values');
                min.setAttribute('required', '');
                min.classList.add('border', 'border-solid', 'p-1', 'rounded-md');

                const minv = document.createElement('p');
                minv.textContent = 'Minimum: '

                minl.appendChild(minv);
                minl.appendChild(min);

                const maxl = document.createElement('label');
                maxl.classList.add('flex', 'items-center', 'space-x-2', 'block', 'text-md', 'text-gray-700',);

                const max = document.createElement('input');
                max.setAttribute('name', 'values');
                max.setAttribute('required', '');
                max.classList.add('border', 'border-solid', 'p-1', 'rounded-md');

                const maxv = document.createElement('p');
                maxv.textContent = 'Maximum: '

                maxl.appendChild(maxv);
                maxl.appendChild(max);

                newFilter.appendChild(minl);
                newFilter.appendChild(maxl);
            }
                
            const valuesF = document.getElementById('valuesF');
            if(!valuesF){
                filter.appendChild(newFilter);
            }
            else{
                valuesF.replaceWith(newFilter);
            }



            if (!sbutton){  //if there is no button
                sbutton = true;
                //Display submit button
                    const submit = document.createElement('button');
                    submit.setAttribute('type', 'submit');
                    submit.classList.add('mt-3', 'w-1/2', 'px-4', 'py-2', 'bg-purple-800', 'text-white', 'rounded-md', 'hover:bg-purple-700', 'focus:outline-none', 'focus:ring-2', 'focus:ring-purple-500', 'focus:ring-offset-2');
                    submit.textContent='Submit';
                    submit.setAttribute('id', 'submit')
                    filter.appendChild(submit);
            }
            if (category == 'broadcast_day_of_the_week' || category == 'genres' || category == 'studios'){
                const form = document.getElementById('filters');
                const checkboxes = form.querySelectorAll('input[type="checkbox"]');
                const em = document.getElementById('em');
                form.addEventListener('submit', function (event) {
                    const isChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);

                    if (!isChecked) {
                        event.preventDefault();
                        em.classList.remove('hidden'); 
                    } else {
                        em.classList.add('hidden');
                    }
                });
            }

        });
    }

    if(page == 'Graph'){
        if(loggedIn){
            const body = document.getElementById('body');
            const favorite = document.createElement('button');
            favorite.setAttribute('type', 'submit');
            favorite.classList.add('mt-3', 'w-1/2', 'px-4', 'py-2', 'bg-purple-800', 'text-white', 'rounded-md', 'hover:bg-purple-700', 'focus:outline-none', 'focus:ring-2', 'focus:ring-purple-500', 'focus:ring-offset-2');
            favorite.textContent = 'Favorite';
            body.appendChild(favorite);
        }
    }
});
