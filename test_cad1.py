import unittest
import cadquery as cq

class MyTestCase(unittest.TestCase):
    def test_robot_mount_plate(self):
        p0 = 110
        wp = cq.Workplane("XY")
        part = wp.box(p0, p0, 40).translate((0,0,4.9))
        void_orin = wp.box(110, 110, 40).translate((0,0,-5))
        void_upper = wp.box(110-40, 110-40, 20).translate((0,0,12.5))
        void_x = wp.box(p0, 110-40, 50).translate((0,0,-2.5))
        void_y = wp.box(110 - 40, p0,50).translate((0,0,-2.5))
        void_d435 = wp.box(20, 90, 55).translate((65,0,-5))
        void_lidar = wp.box(60, 60, 55).translate((-30,0,0))
        void_fan = wp.cylinder(100,30)
        voids = void_orin.union(void_upper).union(void_x).union(void_y).union(void_d435).union(void_lidar).union(void_fan)
        part = part.cut(voids)

        # Export STL
        cq.exporters.export(part, 'part.stl')

if __name__ == '__main__':
    unittest.main()
