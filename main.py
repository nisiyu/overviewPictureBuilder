
import ConfigParser
def main(args):
    s = ConfigParser.Parse()
    s.calc_all_items_height()
    s.align_items()
    s.draw_all()


main(1)