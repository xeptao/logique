export const factorial = (n: number): number => {
  if (n > 1) {
    const m = n - 1;

    return n * factorial(m);
  } else if (n === 1) {
    return 1;
  } else {
    console.log("You can't enter negative values.");
    return 0;
  }
};

