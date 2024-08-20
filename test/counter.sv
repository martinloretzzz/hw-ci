module counter(input logic clk, input logic rst, output logic [3:0] out);

  timeunit 1ns;
  timeprecision 1ns;

  reg [3:0] num = 4'b0000;

  always @(posedge clk) begin
    if (rst == 1'b1) begin
      num <= 4'b0000;
    end
    else begin
      num <= num + 'd1;
    end
  end

  assign out = num;

endmodule
