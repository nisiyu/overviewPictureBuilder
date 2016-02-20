import Builder
def main(args):
    try:
        s = Builder.settings()
        s.test_data()
        s.calc_all_items_height()
        s.align_items()
        s.draw_all()
    except Exception as ex:
        print ex