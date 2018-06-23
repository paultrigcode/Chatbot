


$('button').click(function() {
    var real_sentence = $("#myInput").val();
    var sentence = real_sentence.slice(0,-1) + real_sentence.charAt(real_sentence.length - 1).toLowerCase();
    // console.log(sentence);
        
    var sign = this.value;
    var do_lower_swaps = {a:"à", e:"è", ẹ:"ẹ̀", i:"ì", o: "ò", ọ:"ọ̀", u:"ù", Ọ:"Ò̩"};
    var mi_lower_swaps = {a:"á", e:"é", ẹ:"ẹ́", i:"í", o: "ó", ọ:"ọ́", u:"ú", n:"ń"};
    var dot_swaps = {e: 'ẹ', è: "ẹ̀", é:"ẹ́", o: 'ọ', ò: "ọ̀", ó: "ọ́", s: 'ṣ'}
    var sub = ''
    // alert(sign);
    if (['do', 'mi', 'dot'].indexOf(sign) > -1) {
        var lastChar = sentence.slice(-1)
        if (sign == 'do'){
            sub = do_lower_swaps[lastChar]
            // alert(sub);
        } 
        else if (sign == 'mi'){
            sub = mi_lower_swaps[lastChar]
            // alert(sub);
        }
        else if (sign == 'dot'){
            sub = dot_swaps[lastChar]
            // alert(sub);
        }
    }
    if(real_sentence[real_sentence.length - 1].toUpperCase() == real_sentence[real_sentence.length - 1]){
        // console.log('capital letter detected');
        sub = sub.charAt(0).toUpperCase();  
    }
    if (sub !="" & sub != undefined){
        document.getElementById("myInput").value = real_sentence.slice(0, -1) + sub;
    }   
});

function sendPressed(){
    document.getElementById("myBtn").click();
};
