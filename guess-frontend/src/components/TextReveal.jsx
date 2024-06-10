export const TextRevealTW = () => {
  const text = "Text Reveal Animation 💫";

  return (
    <>
      <h1 className="overflow-hidden text-2xl font-bold leading-6 text-white">
        {Array.from(text).map((char, index) => (
          <span
            className="animate-text-reveal inline-block"
            key={`${char}-${index}`}
            style={{ animationDelay: `${index * 0.05}s` }}
          >
            {char === " " ? "\u00A0" : char}
          </span>
        ))}
      </h1>
    </>
  );
};
