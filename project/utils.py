from fabric.operations import local

class Mailcatcher:
    def __init__(self):
        pass

    def install_gem(self):
        """
        Install up mailcatcher gem.
        Usage: Run locally
        """
        local('gem install mailcatcher')
    def vm_setup(self, host_ip, port, email):
        """
        Set up mailcatcher on VM.
        IMPORTANT: Fabric command should be run as sudo on VM!
        """
        local('yum -y install postfix')
        local('echo "virtual_maps = regexp:/etc/postfix/virtual-regexp\nrelayhost = [%s]:%s" >> /etc/postfix/main.cf' % (host_ip, port))
        local('touch /etc/postfix/virtual-regexp')
        local('echo /.+@.+/  %s > /etc/postfix/virtual-regexp' % email)
        local('/usr/sbin/postmap /etc/postfix/virtual-regexp')
        local('/etc/init.d/postfix restart')
    def start(self, smtp_ip, http_ip):
        """
        Start mailcatcher deamon
        Usage: Run locally
        """
        local("mailcatcher --smtp-ip %s --http-ip=%s" % (smtp_ip, http_ip))
