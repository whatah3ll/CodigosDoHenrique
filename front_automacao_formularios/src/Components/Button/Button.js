import "./Button.css";

function Button({ children, onClickFunc }) {
  return (
    <button
      type="button"
      className="button"
      onClick={() => {
        onClickFunc();
      }}
    >
      {children}
    </button>
  );
}

export default Button;
