$(document).ready(function() {
    "use strict";

    $("#create-store-form").validate({
        errorPlacement: function(error, element) {
            if (element.attr("name") == "store_name") {
                error.insertAfter("#domain-input-group");
            } else {
                error.insertAfter(element);
            }
        },
        rules: {
            store_name: {
                required: true,
                domain: true
            },
            store_email: {
                required: true,
                email: true
            },
            store_phone: {
                required: true
            },
            store_address: {
                required: true
            },
            store_opening: {
                required: true
            }
        },
        messages: {
            store_name: {
                required: empty_store_name,
                domain: invalid_store_name
            },
            store_email: {
                required: empty_email,
                email: invalid_email
            },
            store_phone: {
                required: empty_phone
            },
            store_address: {
                required: empty_address
            },
            store_opening: {
                required: empty_hours
            }
        },
        submitHandler: function(form) {
            var l = Ladda.create(document.querySelector("#submit-form"));
			l.start();
            $.ajax({
                type: "POST",
                url: "/create-store-request",
                data: $(form).serialize(),
                dataType: "json",
                success: function(response) {
                    if (response.redirect) {
                        window.location.replace(response.redirect);
                    } else if (response.domain_exists) {
                        $(form).validate().showErrors({store_name: exists_store_name});
                    } else {
                        if (!response.store_name) {
                            $(form).validate().showErrors({store_name: invalid_store_name});
                        }
                        if (!response.store_email) {
                            $(form).validate().showErrors({store_email: invalid_email});
                        }
                        if (!response.store_phone) {
                            $(form).validate().showErrors({store_phone: invalid_phone});
                        }
                        if (!response.store_address) {
                            $(form).validate().showErrors({store_address: invalid_address});
                        }
                        if (!response.store_opening) {
                            $(form).validate().showErrors({store_opening: invalid_hours});
                        }
                    }
                },
                error: function() {
                    sweetAlert("Oops...", something_went_wrong, "error");
                },
                complete: function() {
                    l.stop();
                }
            });
        }
    });
});
