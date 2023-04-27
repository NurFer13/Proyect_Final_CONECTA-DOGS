import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import PersonalInformation from "../component/Forms/PersonalInformation.jsx";
import useAppContext from "../store/AppContext.js";

const formUser = {
  personalInfo: {
    imageSrc: "https://cdn.pixabay.com/photo/2017/09/08/03/49/couple-2727559_960_720.png",
    mainTitle: "REGISTRO DE USUARIOS",
    secondaryTitle: "Información personal",
    description: "Cuéntanos un poquito acerca de ti.",
    component: <PersonalInformation />
  }
}

const firstStep = "personalInfo";

const SingUpForm = () => {

  const { store, actions } = useAppContext();

  const [currentStep, setCurrentStep] = useState(firstStep);

  const navigate = useNavigate();


  const handleNext = () => {
    if (store.userInput.radioOwnerCarer == "owner") { setCurrentStep("dogInfo") }
    if (store.userInput.radioOwnerCarer == "carer") { setCurrentStep("additionalInfo") }
  };

  const handleBack = () => {
    if (currentStep == firstStep) { return; }
    setCurrentStep("personalInfo");
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    actions.handleRegister(e)

    navigate("/");
  };


  return (
    <>
      <section className="py-4 custom-login">
        <div className="container border border-primary custom-form bg-light">
          <div className="row">
            <h2 className="text-center border border-primary p-4">{formUser[currentStep].mainTitle}</h2>
            {/* IMAGEN */}
            <div className="col-12 col-md-6 py-3">
              <img src={formUser[currentStep].imageSrc} className="img-fluid" />
            </div>
            {/* FORMULARIO */}
            <div className="col-12 col-md-6 py-3">
              <form>
                <h2 className="text-center">{formUser[currentStep].secondaryTitle}</h2>
                <p className="text-center">{formUser[currentStep].description}</p>
                {formUser[currentStep].component}

                <div id="helpLogIn" className="form-text fs-8 fst-italic d-flex justify-content-end py-2">
                  Los campos marcados con * son obligatorios.
                </div>

                <div className="d-grid gap-2 d-md-flex justify-content-md-end py-4">
                  <button className="action-button shadow animate blue" onClick={handleBack} navigate="log-in-form"> Atrás </button>
                  <button className="action-button shadow animate blue" type="submit" onClick={handleSubmit}> Enviar </button>
                </div>


                {/* <div className="d-grid gap-2 d-md-flex justify-content-md-end py-2">
                  <button className="action-button shadow animate blue" onClick={handleBack}> Atrás </button>
                  {currentStep == "personalInfo"
                    ? <button className="action-button shadow animate blue" onClick={handleNext}> Siguiente </button>
                    : <button className="action-button shadow animate blue" type="submit" onClick={handleSubmit}> Enviar </button>
                  }
                </div> */}
              </form>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default SingUpForm;
