var assert = require('assert');

//
// Variáveis
//

var a, b, temp;

//
// Sua lógica
//

a = 999;
b = 555;
temp = a;
a = b;
b = temp;

//
// Seu teste
//

try {
    assert.equal(555, a);
    assert.equal(999, b);
} catch(e) {
    console.log(e);
}