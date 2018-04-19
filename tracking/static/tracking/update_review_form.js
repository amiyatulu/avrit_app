new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data:  {
    title: 'Post Review',
    seen: true,
    updated_seen:false,
    graphics: null,
    concrete: null,
    probing: null,
    elaboration: null,
    solved_problems: null,
    practice: null,
    originality: null,
    errors: null,
    deepness: null,
    preciseness: null,
    cognitive_load: null,
    big_ideas:null,
    evidence: null,
    overall_comments: null,
    dat_link : null,
    backup_link:null,
    form_errors:[],
    post_data:null,
    datap:null,
    updated_data:null,
  },
  methods: {
    submitForm: function (e) {
      this.form_errors = [];
      if(!this.graphics) this.form_errors.push("Graphics required");
      if(!this.concrete) this.form_errors.push("Concrete required.");
      if(!this.probing) this.form_errors.push("Probing required.");
      if(!this.elaboration) this.form_errors.push("Elaboration required.");
      if(!this.solved_problems) this.form_errors.push("solved_problems required.");
      if(!this.practice) this.form_errors.push("practice required.");
      if(!this.originality) this.form_errors.push("originality required.");
      if(!this.errors) this.form_errors.push("errors required.");
      if(!this.deepness) this.form_errors.push("deepness required.");
      if(!this.preciseness) this.form_errors.push("preciseness required.");
      if(!this.cognitive_load) this.form_errors.push("cognitive_load required.");
      if(!this.big_ideas) this.form_errors.push("big_ideas required.");
      if(!this.evidence) this.form_errors.push("evidence required.");
      if(!this.overall_comments) this.form_errors.push("overall_comments required.");
      if(!this.dat_link) this.form_errors.push("dat_link required.");
      if(this.form_errors.length == 0){
        this.datap = {graphics:this.graphics,concrete:this.concrete, probing:this.probing, elaboration:this.elaboration,
                 solved_problems:this.solved_problems, practice:this.practice, originality:this.originality,
                 errors: this.errors, deepness: this.deepness, preciseness: this.preciseness, 
                 cognitive_load: this.cognitive_load, big_ideas:this.big_ideas, evidence:this.evidence,
                 overall_comments:this.overall_comments, dat_link:this.dat_link, backup_link:this.backup_link
        }
        console.log(this.datap)
        this.$http.post(ajaxreview, this.datap, {
           headers: {'X-CSRFToken': csrftoken}
        }).then(response => {
        response.status;
        response.statusText;
        response.headers.get('Expires');
        this.post_data = response.body;
        console.log(this.post_data);
        this.seen = false;
        this.updated_seen = true;
        this.updated_data = this.post_data

        }, response => {
    // error callback
      });
        
        
        
    
      };
      
     
    },
    editForm: function(){
      this.seen=true;
      this.updated_seen=false;
    }
  }
})