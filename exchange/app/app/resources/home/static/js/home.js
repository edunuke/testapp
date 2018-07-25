var landingPageController = {
	/* Set elememnt name tag, class, id, identifiers*/
	toggleFormElementName : ".message a",
	loginElementName : "#submit",
	registerElementName : "#register-submit",

	findElements: function () {
		/* Turn elements into jquery objects */
		var base = this;
		base.toggleFormElement = $(base.toggleFormElementName);
		base.loginElement = $(base.loginElementName);
		base.registerElement = $(base.registerElementName);
		return base;
	},

	globalEvents: function () {
		var base = this;
		base.toggleFormElement.on("click",function () {
			 $('form').animate({height: "toggle", opacity: "toggle"}, "slow")	
		})

		return base;

	},
    
    login: function() {
        var base = this;

        base.loginElement.click('click', function(e) {

            e.preventDefault();
            var data = $('.login-form').serialize()
            console.log(data)
            $.ajaxSetup({
               headers:'{{csrf_token}}'
            });     

            $.ajax({
                url: "/main/",
                //data: JSON.stringify(data),
                data: data,
                type: 'POST',
                //contentType: "application/json",
                beforeSend: function () {
                    $('.login-form span').remove()
                    $('#loader-wrapper').fadeIn(500)

                },
                success: function(response) {
                    timer = 2000;
                    if (response.status == 'error') {
                        console.log('error')
                        console.log(response.message)
                        $('.login-form span').remove()
                        $('.login-form').append('<span>'+response.message+'</span>')
                        setTimeout(function () {
                            $('#loader-wrapper').fadeOut(500);
                        },timer);


                    } else if (response.status == 'validation') {
                        console.log('validation')
                        $('.login-form').remove('span');

                        setTimeout(function () {
                            $('#loader-wrapper').fadeOut(500);
                        }, timer + 2000);
                        
                        

                        Object.keys(response.message).map(e => console.log(`key=${e}  value=${response.message[e]}`));
                        
                    } else {
                        $('.login-form').remove('span')
                        console.log('im good')
                        setTimeout(function () {
                            //console.log(response.message)
                            window.location = response.message;
                        },timer);
                        
                        
                    } 
                },
                error: function(response) {
                    console.log(response);
                }
            });
        });

        return base

    },

    register: function() {
        var base = this;

        base.registerElement.on('click', function(e) {

        	e.preventDefault();

        	//var data = $(".register-form").serializeArray();
            var data = $('.register-form').serialize()

        	$.ajaxSetup({
        		headers:'{{csrf_token}}}'
        	});

            $.ajax({
                url: "/users/",
                //data: JSON.stringify(data),
                data: data,
                type: 'POST',
                //contentType: "application/json",
                beforeSend: function () {
                    console.log(data)
                },
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        });

        return base

	},
    
    initialize: function () {
        var base = this;
        
        base.findElements().globalEvents().login().register()
    }

}

$(document).ready(function() {
    landingPageController.initialize();
    
});
