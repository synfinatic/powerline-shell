ROLENAME='/usr/bin/rolename'
from ..utils import py3, BasicSegment

def _get_hostorrole():
    import os
    import subprocess
    from socket import getfqdn
    if not os.path.isfile(ROLENAME):
        return getfqdn().split('.')[0]

    # apple
    host = ""
    try:
        host = subprocess.check_output([ROLENAME]).rstrip()
    except subprocess.CalledProcessError:
        host = getfqdn().split('.')[0]
    # return the rolename.datacenter
    return "%s.%s" % (host, getfqdn().split('.')[1])

def _get_rootindicator(powerline):
    root_indicators = {
        'bash': ' \\$ ',
        'zsh': ' %# ',
        'bare': ' $ ',
    }
    bg = powerline.theme.CMD_PASSED_BG
    fg = powerline.theme.CMD_PASSED_FG
    return root_indicators[powerline.args.shell]

class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        import os
        if powerline.args.shell == 'bash':
            user_prompt = ' \\u'
        elif powerline.args.shell == 'zsh':
            user_prompt = ' %n'
        else:
            user_prompt = ' %s' % os.getenv('USER')

        hostname = _get_hostorrole()
        userhost = user_prompt + '@' + hostname + _get_rootindicator(powerline)
        if powerline.segment_conf("hostname", "colorize"):
            from ...color_compliment import stringToHashToColorAndOpposite
            from ..colortrans import rgb2short
            FG, BG = stringToHashToColorAndOpposite(hostname)
            FG, BG = (rgb2short(*color) for color in [FG, BG])
            powerline.append(userhost, FG, BG)
        else:
            powerline.append(userhost,
                             powerline.theme.HOSTNAME_FG,
                             powerline.theme.HOSTNAME_BG)
