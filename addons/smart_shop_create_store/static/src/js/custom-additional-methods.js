$.validator.addMethod("domain", function(value, element) {
    return this.optional(element) || /^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]$/.test(value);
}, "Please specify a valid domain name");
