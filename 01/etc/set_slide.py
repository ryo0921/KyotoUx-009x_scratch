from IPython.display import HTML
HTML('''<style>.CodeMirror{min-width:100% !important;}</style>''')
from traitlets.config.manager import BaseJSONConfigManager
path = "/Users/ryoichi/anaconda/etc/jupyter/nbconfig"
cm = BaseJSONConfigManager(config_dir=path)
w='1600'
h='900'
cm.update('livereveal', {
        'theme'             : 'simple',
        'transition'        : 'slide',
        'start_slideshow_at': 'selected',
        'slideNumber'       : 'true',
        'history'           : 'true',
        'center'            : 'false',
        'width'             : w,
        'height'            : h,
        'margin'            : '0.0',
        'scroll'            : 'true',
#        'minScale'          : '0.2',
#        'maxScale'          : '1.0',
})
print(w,'x',h)
