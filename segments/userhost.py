def add_userhost_segment(powerline):
    import os
    if powerline.args.shell == 'bash':
        user_prompt = ' \\u'
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n'
    else:
        user_prompt = ' %s' % os.getenv('USER')

    if os.getenv('USER') == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
    else:
        bgcolor = Color.USERNAME_BG

    #powerline.append(user_prompt, Color.USERNAME_FG, bgcolor)
    if powerline.args.colorize_hostname:
        from lib.color_compliment import stringToHashToColorAndOpposite
        from lib.colortrans import rgb2short
        from socket import gethostname
        hostname = gethostname()
        FG, BG = stringToHashToColorAndOpposite(hostname)
        FG, BG = (rgb2short(*color) for color in [FG, BG])
        host_prompt = '%s ' % hostname.split('.')[0]

        userhost = user_prompt + '@' + host_prompt
        powerline.append(userhost, FG, BG)
    else:
        if powerline.args.shell == 'bash':
            host_prompt = '\\h '
        elif powerline.args.shell == 'zsh':
            host_prompt = '%m '
        else:
            import socket
            host_prompt = '%s ' % socket.gethostname().split('.')[0]

        userhost = user_prompt + '@' + host_prompt
        powerline.append(userhost, Color.HOSTNAME_FG, Color.HOSTNAME_BG)
