import java.util.Scanner;

class SalaryCalculator {
    public static double calculateGross(double basic, double allowance) {
        return basic + allowance;
    }

    public static double calculateNet(double gross, double deduction) {
        return gross - deduction;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double basicSalary = scanner.nextDouble();
        double allowance = scanner.nextDouble();
        double deduction = scanner.nextDouble();

        double grossSalary = SalaryCalculator.calculateGross(basicSalary, allowance);
        double netSalary = SalaryCalculator.calculateNet(grossSalary, deduction);

        System.out.println("Gross Salary = " + (int) grossSalary);
        System.out.println("Net Salary = " + (int) netSalary);

        scanner.close();
    }
}
