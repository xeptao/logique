import factorial from "../src/factorial";

describe("factorial", () => {
  test("should correctly calculate values", () => {
    const result = factorial(3);

    expect(result).toEqual(6);
  });
});
