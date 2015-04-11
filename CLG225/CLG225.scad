// Units are in mm
height = 1.06;
width = 13;
length = 13;
pitch = 0.8;
ballwidth = 0.4;

translate([-width/2, -length/2, ballwidth/2]) {
    color([40/255, 40/255, 40/255]) {
        difference() {
            cube([width, length, height]);
            translate([2, 2, height - 0.15]) {
                cylinder(r = .5, $fn = 100);
            }
        }
    }
}

for (i = [-7:7]) {
        for (j = [-7:7]) {
            translate([i*pitch, j*pitch, ballwidth/2]) {
                color("silver") {
                    sphere(r = ballwidth/2, $fn = 20);
                }
            }
        }
    }