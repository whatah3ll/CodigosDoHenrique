import Container from "../../Components/Container/Container";
import FileAdd from "../../Components/FileAdd/FileAdd";
import Footer from "../../Components/Footer/Footer";
import Header from "../../Components/Header/Header";

import "./Home.css";

function Home() {
  return (
    <main>
      <Header />
      <Container>
        <FileAdd />
      </Container>
      <Footer />
    </main>
  );
}

export default Home;
