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


                },
                success: function(response) {
                    timer = 2000;
                    if (response.status == 'error') {
                        $("input.oops").removeClass("oops");
                        Object.keys(response.message).map(e => $(".login-form #" + e).addClass("oops"));



                    } else if (response.status == 'validation') {
                        $("input.oops").removeClass("oops");
                        Object.keys(response.message).map(e => $(".login-form #" + e).addClass("oops"));

                        
    
                       // Object.keys(response.message).map(e => $('.login-form').append('<span>'+`key=${e}  value=${response.message[e]}`+'</span>'));
                        
                    } else {
                        $('.login-form').remove('span')
                        $('canvas').hide()
                        $('.login-page').hide()
                        $('#loader-wrapper').fadeIn('slow', function () {
                            window.location = response.message;
                        })


                        
                        
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
