#include <iostream>
using namespace std;

//Parent Class
class Parent{
  public:
    Parent();
    //Public int
    int my_pub;
   // virtual function
    virtual void who_this(){cout << "Parent" <<endl;}
    //Accessors and mutators
    void set_priv(int x){my_priv=x;}
    int get_priv(){return my_priv;}
    void set_prct(int x){my_prct=x;}
    int get_prct(){return my_prct;}
  //Protected and private variables
  protected:
    int my_prct;
  private:
    int my_priv;
};
//Parent Constructor
Parent::Parent(){
	my_pub=1;
	my_prct=2;
	my_priv=3;
}

class Child: public Parent {
  public:
    Child();
   //Overridden function
    void who_this(){cout << "Child" <<endl;}
};
//Child constructur
Child::Child(){
	my_prct=4;//Can access proteted
}

int main () {
//Creat instances and place them into polymorphic pointers
  Parent p;
  Child c;
  Parent * pp1 = &p;
  Parent * pp2 = &c;

//Double check who they are
  cout << "Who is p?" << endl;
  pp1->who_this();
  cout << "Who is c?" << endl;
  pp2->who_this();

//Check that child was construcetd with different protected variable
  cout << "What is c protecting?"<< endl << pp2->get_prct() << endl;
  cout << "What is p protecting?"<< endl << pp2->get_prct() << endl;

//See if that variable can be set with appropriate function
  pp2->set_prct(5);
  cout << "What is c protecting now?"<< endl << pp2->get_prct() << endl;
 
  return 0;
}
