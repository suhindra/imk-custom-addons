# coding: utf-8
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from openerp import exceptions
from openerp import models, fields, api, _


to_19_id = (u'Nol', 'Satu', 'Dua', 'Tiga', 'Empat', 'Lima', 'Enam',
          'Tujuh', 'Delapan', 'Sembilan', 'Sepuluh', 'Sebelas', 'Dua Belas', 'Tiga Belas',
          'Empat Belas', 'Lima Belas', 'Enam Belas', 'Tujuh Belas', 'Delapan Belas', 'Sembilan Belas')
tens_id = ( 'Dua Puluh', 'Tiga Puluh', 'Empat Puluh', 'Lima Puluh', 'Enam Puluh', 'Tujuh Puluh', 'Delapan Puluh', 'Sembilan Puluh')
denom_id = ('',
          'Ribu', 'Juta', 'Milyar')

def _convert_nn_id(val):
    """ convert a value < 100 to Indonesian
    """
    if val < 20:
        return to_19_id[val]
    for (dcap, dval) in ((k, 20 + (10 * v)) for (v, k) in enumerate(tens_id)):
        if dval + 10 > val:
            if val % 10:
                if dval == 70 or dval == 90:
                    return tens_id[dval / 10 - 3] + '-' + to_19_id[val % 10 + 10]
                else:
                    return dcap + '-' + to_19_id[val % 10]
            return dcap

def _convert_nnn_id(val):
    """ convert a value < 1000 to Indonesian
    
        special cased because it is the level that kicks 
        off the < 100 special case.  The rest are more general.  This also allows you to
        get strings in the form of 'forty-five hundred' if called directly.
    """
    word = ''
    (mod, rem) = (val % 100, val // 100)
    if rem > 0:
        if rem == 1:
            word = 'Seratus'
        else:
            word = to_19_id[rem] + ' Ratus'
        if mod > 0:
            word += ' '
    if mod > 0:
        word += _convert_nn_id(mod)
    return word

def indonesian_number(val):
    if val < 100:
        return _convert_nn_id(val)
    if val < 1000:
        return _convert_nnn_id(val)
    for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom_id))):
        if dval > val:
            mod = 1000 ** didx
            l = val // mod
            r = val - (l * mod)
            if l == 1:
                ret = denom_id[didx]
            else:
                ret = _convert_nnn_id(l) + ' ' + denom_id[didx]
            if r > 0:
                ret = ret + ', ' + indonesian_number(r)
            return ret

def amount_to_text_id(numbers, currency):
    number = '%.2f' % numbers
    units_name = currency
    liste = str(number).split('.')
    start_word = indonesian_number(abs(int(liste[0])))
    
    final_result = start_word + ' ' + units_name
    return final_result 
