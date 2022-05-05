export const fibonacci = (n: number): number => {
  if (n > 2) {
    return fibonacci(n - 1) + fibonacci(n - 2);
  } else if (n === 1 || n === 2) {
    return 1;
  } else {
    console.log("Do not enter negative values.");

    return 0;
  }
};
