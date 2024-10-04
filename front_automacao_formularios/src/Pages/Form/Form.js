import Container from "../../Components/Container/Container";
import Footer from "../../Components/Footer/Footer";
import Header from "../../Components/Header/Header";
import AutoForm from "../../Components/AutoForm/AutoForm";

import "./Form.css";

function Form() {
  return (
    <main>
      <Header />
      <Container>
        <AutoForm></AutoForm>
      </Container>
      <Footer />
    </main>
  );
}

export default Form;
