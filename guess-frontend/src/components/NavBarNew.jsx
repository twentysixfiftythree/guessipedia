const NavBarNew = () => {
  return (
    <nav className="nav">
      <a href="/" className="site-title">
        Guessipedia
      </a>
      <ul>
        <li>
          <a href="/settings">Settings</a>
        </li>
        <li>
          <a href="/">Github</a>
        </li>
        <li>
          <a href="/">About</a>
        </li>
      </ul>
    </nav>
  );
};

export default NavBarNew;
