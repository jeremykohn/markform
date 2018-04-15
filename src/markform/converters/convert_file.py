from os.path import basename, dirname, isdir, isfile, join
from convert_text import convert_text

def convert_file(input_filepath, custom_output_filename=None, overwrite_file=False):
    # Create output filepath. Custom filename if specified, otherwise automatically generated.
    if custom_output_name:
        output_filepath = join(dirname(input_filepath), custom_output_filename)
    else:
        output_filepath = join(dirname(input_filepath), "converted_" + basename(input_filepath))

    # Read text from Markform document.
    with open(input_filepath, 'r') as infile:
        input_text = infile.read()

    # Convert text.
    output_text = convert_text(input_text)

    # Check if file exists, and if so whether it should be overwritten.
    if not isfile(input_filepath) or overwrite_file == True:
        # OK to write converted text to file.
        with open(output_filepath, 'w') as outfile:
            outfile.write(output_text)
    else:
        # Don't overwrite file.
        raise ValueError("Must specify `overwrite_file=True`, or the Markform converter will not overwrite the existing file {}".format(basename(input_filepath), dirname(input_filepath)))
