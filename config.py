# This is the configuration file for your powerline-shell prompt
# Every time you make a change to this file, run install.py to apply changes
#
# For instructions on how to use the powerline-shell.py script, see the README

# Add, remove or rearrange these segments to customize what you see on the shell
# prompt. Any segment you add must be present in the segments/ directory

SEGMENTS = [
    'newline',
    'set_term_title',
    'time',
    'userhost',

#    'ssh',

    'cwd',
    'read_only',

#    'virtual_env',

#    'hostname',
    #'jobs',
    'exit_code',
#    'fossil',

    'newline',
#    'jobs',
    'git',
    'hg',
    'svn',

# Shows a '#' if the current user is root, '$' otherwise
# Also, changes color if the last command exited with a non-zero error code
    'root',
]

# Change the colors used to draw individual segments in your prompt
THEME = 'default'
