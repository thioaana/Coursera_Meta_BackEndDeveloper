from rest_framework.permissions import BasePermission
    
class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Manager'):
            return True
        return False

class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Delivery-Crew'):
            return True
        return False
    
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        return False
    
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user :
            if  not request.user.is_superuser and not request.user.groups.filter(name=['Manager', 'Delivery-Crew']) :
                return True
        return False 
