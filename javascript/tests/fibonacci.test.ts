import fibonacci from "../src/fibonacci";

describe("factorial", () => {
  test("should correctly calculate any input", () => {
    const result = fibonacci(6);

    expect(result).toEqual(8);
  });

  test("should correctly calculate 1 and 2", () => {
    const resultOne = fibonacci(1);
    const resultTwo = fibonacci(2);

    expect(resultOne).toEqual(1);
    expect(resultTwo).toEqual(1);
  });

  test("should correctly handle edge case", () => {
    const result = fibonacci(-1);

    expect(result).toEqual(0);
  });
});
