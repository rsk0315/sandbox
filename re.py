(
  r'(?:foo)+(bar)*[baz]?[^qux]+?'
  r'.^$'
  r'quux{2,3}'
  r'corge{2}'
  r'grault{,4}'
  r'\\\.\^\$\*\+\?\{\x00\u0000\U00000000\x[]'
  r'|(?iLmsuxc)(?P<NAME>...)(>P=NAME)(?#COMMENT)'
  r'(?=)(?!)(?<=)(?<!)(?(id/name)yes|no)\A\Z\b\B\g<1>\2\D\w'
)