class BaseController {
    constructor() {
        this._selectIdioma = document.querySelector("#linguagem");
        this._csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    }

    AlteraIdioma(idioma){
        event.preventDefault();
        console.log(this._selectIdioma.value);
        let form = document.createElement("form");
        form.setAttribute("method", "post");
        form.setAttribute("action", "/i18n/setlang/");

        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);

        form.appendChild(hiddenField);
        document.body.appendChild(form);
        form.submit();



    }


}