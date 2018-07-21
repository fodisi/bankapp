#!/usr/bin/env python3


import os


class BaseView():

    BORDER_LINE_CHAR = '#'
    ALIGN_CENTER = '^'
    ALIGN_LEFT = '<'
    ALIGN_RIGHT = '>'

    """Cleans the terminal window."""
    @staticmethod
    def clear_screen():
        # windows(NT) => cls; unix/linux => clear
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self, screen_width=80):
        self.width = 0
        self.__line_width = 0
        self.__title_pattern = ''
        self.resize_screen(screen_width)

    def resize_screen(self, screen_width):
        self.width = screen_width
        # Needs -4 chars so it counts for 04 formatting chars => '# {line} #'
        self.__line_width = screen_width - 4
        self.__title_pattern = self.get_line_pattern(BaseView.ALIGN_CENTER)

    def __print_app_name(self):
        self.print_border_line()
        print(self.__title_pattern.format('BANKAPP TERMINAL'))
        self.print_border_line()

    def fill_with(self, text, total_length, character=' '):
        pattern = '{text}{{0:{ch}>{length}}}'
        fill_length = total_length - len(text)
        pattern = pattern.format(text=text, ch=character, length=fill_length)
        return pattern.format(character)

    def get_line_pattern(self, alignment):
        pattern = '{ch} {{0:{align}{width}}} {ch}'
        return pattern.format(ch=BaseView.BORDER_LINE_CHAR,
                              align=alignment,
                              width=str(self.__line_width))

    def clear(self):
        BaseView.clear_screen()
        self.__print_app_name()

    def print_border_line(self):
        print(self.width * BaseView.BORDER_LINE_CHAR)

    def print_line_divider(self):
        divider = self.fill_with('-', self.__line_width, '-')
        print('{ch} {divider} {ch}'.format(ch=BaseView.BORDER_LINE_CHAR,
                                           divider=divider))

    def print_empty_header_line(self):
        print(self.__title_pattern.format(''))

    def print_empty_lines(self, count):
        for _ in range(count):
            print('')

    def print_header(self, title, *header_lines):
        line_pattern = self.get_line_pattern(BaseView.ALIGN_LEFT)
        self.clear()

        # Prints screen title and header lines
        self.print_empty_header_line()
        print(self.__title_pattern.format(title.upper()))
        self.print_empty_header_line()
        self.print_border_line()

        # Prints header lines
        if len(header_lines) > 0:
            self.print_empty_header_line()
            for line in header_lines:
                print(line_pattern.format(line))
            self.print_empty_header_line()
            self.print_border_line()

    def show_message(self, title, message, clean_screen=False):
        if clean_screen == True:
            self.clear()

        self.print_empty_lines(2)
        print('{0}'.format(title.upper()))
        print(self.fill_with('-', self.width, '-'))
        print('{0}'.format(message))
        self.wait_for_user()

    def wait_for_user(self):
        print('\n\n\n\n\nPress ENTER to continue...')
        input()


if __name__ == '__main__':

    view = BaseView(74)

    view.resize_screen(80)
    assert view.width == 80, 'Error at view.resize_screen'

    # BaseView.fill_with - Asserts format label returns a string with the desired length
    assert len(view.fill_with('text', 10)) == 10, ('Error at view.fill_with')

    # BaseView.get_line_pattern
    #
    # Asserts CENTER alignment
    ch = BaseView.BORDER_LINE_CHAR
    expected = ch + ' {0:^76} ' + ch
    assert view.get_line_pattern(BaseView.ALIGN_CENTER) == expected, (
        'Error at view.get_line_pattern(BaseView.ALIGN_CENTER)')
    # Asserts LEFT alignment
    expected = ch + ' {0:<76} ' + ch
    assert view.get_line_pattern(BaseView.ALIGN_LEFT) == expected, (
        'Error at view.get_line_pattern(BaseView.ALIGN_LEFT)')
    # Asserts RIGHT alignment
    expected = ch + ' {0:>76} ' + ch
    assert view.get_line_pattern(BaseView.ALIGN_RIGHT) == expected, (
        'Error at view.get_line_pattern(BaseView.ALIGN_RIGHT)')

    # BaseView.clear()
    view.clear()

    # BaseView.print_border_line
    view.print_border_line()

    # BaseView.print_line_divider
    view.print_line_divider()

    # BaseView.print_empty_header_line
    view.print_empty_header_line()

    input()

    # BaseView.print_header
    # Tests header with additional lines
    view.print_header('title', 'line1', 'line2')
    input()

    # Tests header with no additional lines
    view.print_header('title')
    input()

    # BaseView.show_message
    #
    # shows message without cleaning the screen
    view.show_message('title', 'message')
    # shows message cleaning the screen
    view.show_message('title', 'message', True)

    # BaseView.print_empty_lines - prints 03 empty lines
    print('printing empty lines')
    view.print_empty_lines(3)
    print('printed empty lines')

    # BaseView.print_line_divider
    view.print_line_divider()

    # BaseView.wait_for_user
    view.wait_for_user()
